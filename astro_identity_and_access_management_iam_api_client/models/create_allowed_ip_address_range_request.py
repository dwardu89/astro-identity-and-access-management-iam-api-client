from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateAllowedIpAddressRangeRequest")


@_attrs_define
class CreateAllowedIpAddressRangeRequest:
    """
    Attributes:
        ip_address_range (str): The allowed IP address range in CIDR format. Example: 1.1.1.1/32.
    """

    ip_address_range: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ip_address_range = self.ip_address_range

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ipAddressRange": ip_address_range,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ip_address_range = d.pop("ipAddressRange")

        create_allowed_ip_address_range_request = cls(
            ip_address_range=ip_address_range,
        )

        create_allowed_ip_address_range_request.additional_properties = d
        return create_allowed_ip_address_range_request

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
