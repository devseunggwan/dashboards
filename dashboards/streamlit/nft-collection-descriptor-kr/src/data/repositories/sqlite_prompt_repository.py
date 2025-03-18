import sqlite3
from datetime import datetime
from typing import Optional

from domain.entities.prompt import Completion, Prompt
from domain.repositories.prompt_repository import PromptReopsitory


class SqlitePromptRepository(PromptReopsitory):
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._initialize_db()

    def _initialize_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS prompts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL,
                CREATED_AT TIMESTAMP NOT NULL
            )
            """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS completions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                prompt_id INTEGER NOT NULL,
                content TEXT NOT NULL,
                model_used TEXT NOT NULL,
                created_at TIMESTAMP NOT NULL,
                FOREIGN KEY (prompt_id) REFERENCES prompts (id)
            )
            
            """
        )

        conn.commit()
        conn.close()

    def save_prompt(self, prompt: Prompt) -> Prompt:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        __query = "INSERT INTO prompts (content, created_at) VALUES (?, ?)"
        cursor.execute(__query, (prompt.content, prompt.created_at))
        prompt_id = cursor.lastrowid

        conn.commit()
        conn.close()

        return Prompt(id=prompt_id, content=prompt.content, created_at=prompt.created_at)

    def save_completion(self, completion: Completion) -> Completion:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        __query = """
        INSERT INTO completions (prompt_id, content, model_used, created_at) VALUES (?, ?, ?, ?)
        """
        cursor.execute(
            __query,
            (
                completion.prompt_id,
                completion.content,
                completion.model_used,
                completion.created_at,
            ),
        )

        completion_id = cursor.lastrowid
        conn.commit()
        conn.close()

        return Completion(
            id=completion_id,
            prompt_id=completion.prompt_id,
            content=completion.content,
            model_used=completion.model_used,
            created_at=completion,
        )

    def get_history(self, limit: int = 10) -> list[tuple[Prompt, Completion]]:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        __query = """
            SELECT
                p.id,
                p.content,
                p.created_at,
                c.id,
                c.content,
                c.model_used,
                c.created_at
            FROM
                prompt p
            JOIN
                completions c ON p.id = c.prompt_id
            ORDER BY
                p.created_at DESC
            LIMIT
                ?
        """
        cursor.execute(__query, (limit,))

        results = []

        for row in cursor.fetchall():
            prompt = Prompt(id=row[0], content=row[1], created_at=datetime.fromisoformat(row[2]))
            completion = Completion(
                id=row[3],
                prompt_id=prompt.id,
                content=row[4],
                model_used=row[5],
                created_at=datetime.fromisoformat(row[6]),
            )
            results.append((prompt, completion))

        conn.close()

        return results

    def get_prompt_by_id(self, prompt_id: int) -> Optional[Prompt]:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        __query = """
            SELECT
                id,
                content,
                created_at
            FROM
                prompts
            WHERE
                id = ?
        """
        cursor.execute(__query, (prompt_id,))
        row = cursor.fetchone()
        conn.close()

        return Prompt(id=row[0], content=row[1], created_at=datetime.fromisoformat(row[2])) if row else None
