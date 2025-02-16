from podium.converters._classes import FieldConverter
from podium.converters.field import _queries


replace = FieldConverter(
    name="Replace Values",
    converter=_queries.replace,
)

replace_all = FieldConverter(
    name="Replace All Values",
    validator=_queries.replace_all,
)

to_datetime = FieldConverter(
    name="Cast Datetime",
    validator=_queries.to_datetime,
)

to_lowercase = FieldConverter(
    name="Convert to Lowercase",
    converter=_queries.to_lowercase,
)

to_upppercase = FieldConverter(
    name="Convert to Uppercase",
    validator=_queries.to_uppercase,
)
