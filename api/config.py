from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    # Your other settings...

    database_url: str = Field(..., alias='DATABASE_URL')

    @property
    def DATABASE_URL(self) -> str:
        return self.database_url

    class Config:
        env_file = '.env'
        allow_population_by_field_name = True
