from enum import Enum


class UpdateUserRolesRequestOrganizationRole(str, Enum):
    ORGANIZATION_BILLING_ADMIN = "ORGANIZATION_BILLING_ADMIN"
    ORGANIZATION_MEMBER = "ORGANIZATION_MEMBER"
    ORGANIZATION_OWNER = "ORGANIZATION_OWNER"

    def __str__(self) -> str:
        return str(self.value)
