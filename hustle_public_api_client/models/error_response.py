from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ErrorResponse")


@_attrs_define
class ErrorResponse:
    """
    Attributes:
        code (float): Error code; usually the status code.
        message (str): Error message detailing the error.
        hustle_error_code (Union[Unset, str]): Sometimes available (generally with 422 responses). If the message is not
            descriptive enough to help identify the issue, pass this code to Hustle support.
    """

    code: float
    message: str
    hustle_error_code: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        code = self.code

        message = self.message

        hustle_error_code = self.hustle_error_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "code": code,
                "message": message,
            }
        )
        if hustle_error_code is not UNSET:
            field_dict["hustleErrorCode"] = hustle_error_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code")

        message = d.pop("message")

        hustle_error_code = d.pop("hustleErrorCode", UNSET)

        error_response = cls(
            code=code,
            message=message,
            hustle_error_code=hustle_error_code,
        )

        return error_response
