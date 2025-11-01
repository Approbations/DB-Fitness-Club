from fastapi import Depends, HTTPException, status
from auth.utils import get_current_user, TokenData


def require_client_role(
        current_user: TokenData = Depends(get_current_user)
) -> TokenData:
    if current_user.role != "client":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: client role required"
        )
    return current_user


def require_admin_role(
        current_user: TokenData = Depends(get_current_user)
) -> TokenData:
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: admin role required"
        )
    return current_user
