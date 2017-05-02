##
# Copyright (c) 2008-present MagicStack Inc.
# All rights reserved.
#
# See LICENSE for details.
##


import abc
import datetime
import numbers
import uuid


class Literal(metaclass=abc.ABCMeta):
    pass


Literal.register(numbers.Number)
Literal.register(uuid.UUID)
Literal.register(str)
Literal.register(bytes)
Literal.register(datetime.datetime)
Literal.register(datetime.date)
Literal.register(datetime.timedelta)
Literal.register(datetime.time)
Literal.register(type(None))
