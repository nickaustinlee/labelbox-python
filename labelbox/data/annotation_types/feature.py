from typing import Optional

from pydantic import BaseModel, root_validator

from .types import Cuid


class FeatureSchema(BaseModel):
    """
    Class that represents a feature schema.
    Could be a annotation, a subclass, or an option.
    Schema ids might not be known when constructing these objects so both a name and schema id are valid.

    Use `LabelCollection.assign_schema_ids` or `LabelGenerator.assign_schema_ids`
    to retroactively add schema ids by looking them up from the names.
    """
    name: Optional[str] = None
    schema_id: Optional[Cuid] = None

    @root_validator
    def must_set_one(cls, values):
        if values['schema_id'] is None and values['name'] is None:
            raise ValueError(
                "Must set either schema_id or name for all feature schemas")
        return values
