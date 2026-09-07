from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.clients.auth_client import verify_token_with_auth_service

security = HTTPBearer()

# here check role based access control, and also attach the raw token for forwarding to other services

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Validates token via Auth Service and attaches the raw token for forwarding."""
    token = credentials.credentials
    user_data = await verify_token_with_auth_service(token)

    user_data["raw_token"] = token

    return user_data

class RoleChecker:

    def __init__(self, allowed_roles: list):
        self.allowed_roles = allowed_roles

    def __call__(self, user_data: dict = Depends(get_current_user)):
        user_role = user_data.get("role")
        if user_role not in self.allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to access this resource"
            )
        return user_data