from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_team_roles_request_organization_role import UpdateTeamRolesRequestOrganizationRole
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workspace_role import WorkspaceRole


T = TypeVar("T", bound="UpdateTeamRolesRequest")


@_attrs_define
class UpdateTeamRolesRequest:
    """
    Attributes:
        organization_role (UpdateTeamRolesRequestOrganizationRole): The Team's Organization roles. Example:
            ORGANIZATION_MEMBER.
        workspace_roles (Union[Unset, List['WorkspaceRole']]): The Team's updated Workspace roles. The Workspaces you
            specify must belong to the Team's Organization.
    """

    organization_role: UpdateTeamRolesRequestOrganizationRole
    workspace_roles: Union[Unset, List["WorkspaceRole"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        organization_role = self.organization_role.value

        workspace_roles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.workspace_roles, Unset):
            workspace_roles = []
            for workspace_roles_item_data in self.workspace_roles:
                workspace_roles_item = workspace_roles_item_data.to_dict()

                workspace_roles.append(workspace_roles_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organizationRole": organization_role,
            }
        )
        if workspace_roles is not UNSET:
            field_dict["workspaceRoles"] = workspace_roles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.workspace_role import WorkspaceRole

        d = src_dict.copy()
        organization_role = UpdateTeamRolesRequestOrganizationRole(d.pop("organizationRole"))

        workspace_roles = []
        _workspace_roles = d.pop("workspaceRoles", UNSET)
        for workspace_roles_item_data in _workspace_roles or []:
            workspace_roles_item = WorkspaceRole.from_dict(workspace_roles_item_data)

            workspace_roles.append(workspace_roles_item)

        update_team_roles_request = cls(
            organization_role=organization_role,
            workspace_roles=workspace_roles,
        )

        update_team_roles_request.additional_properties = d
        return update_team_roles_request

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
