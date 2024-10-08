from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeploymentRole")


@_attrs_define
class DeploymentRole:
    """
    Attributes:
        deployment_id (str): The Deployment ID. Example: clm8t5u4q000008jq4qoc3031.
        role (str): The name of the role for the subject in the Deployment. Example: DEPLOYMENT_ADMIN.
    """

    deployment_id: str
    role: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        deployment_id = self.deployment_id
        role = self.role

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deploymentId": deployment_id,
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        deployment_id = d.pop("deploymentId")

        role = d.pop("role")

        deployment_role = cls(
            deployment_id=deployment_id,
            role=role,
        )

        deployment_role.additional_properties = d
        return deployment_role

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
