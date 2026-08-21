import httpx
from fastapi import HTTPException, status
from app.core.config import settings

async def verify_token_with_auth_service(token: str) -> dict:
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                settings.AUTH_SERVICE_URL,
                json={"token": token}
            )
            
            if response.status_code != 200:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid or expired token"
                )
                
            data = response.json()
            if not data.get("valid"):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Token verification failed"
                )
            return data
            
        except httpx.RequestError:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Authentication service is unreachable"
            )