import httpx
from fastapi import HTTPException, status
from app.core.config import settings

async def verify_student_exists(student_id: int, token: str) -> bool:
    """Calls the Student Service to ensure the student exists before marking attendance."""
    async with httpx.AsyncClient() as client:
        try:
            # We must forward the JWT token because the Student Service requires authentication!
            headers = {"Authorization": f"Bearer {token}"}
            response = await client.get(
                f"{settings.STUDENT_SERVICE_URL}/{student_id}",
                headers=headers
            )
            
            if response.status_code == 404:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Student ID {student_id} not found in Student Service"
                )
            
            if response.status_code != 200:
                raise HTTPException(
                    status_code=response.status_code,
                    detail="Error communicating with Student Service"
                )
                
            return True
            
        except httpx.RequestError:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Student Service is currently unreachable"
            )