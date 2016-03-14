#!/usr/bin/env python

import six


@six.python_2_unicode_compatible
class Computation(object):  # pragma: no cover
    """
    An operation that takes a table and produces a new column by performing
    some computation on each row. Computations are invoked with
    :class:`.TableSet.compute`.

    When implementing a custom subclass, ensure that the values returned by
    :meth:`run` are of the type specified by :meth:`get_computed_data_type`.
    This can be ensured by using the :meth:`.DataType.cast` method. See
    :class:`Formula` for an example.
    """
    def __str__(self):
        """
        String representation of this column. May be used as a column name in
        generated tables.
        """
        return self.__class__.__name__

    def get_computed_data_type(self, table):
        """
        Returns an instantiated :class:`.DataType` which will be appended to
        the table.
        """
        raise NotImplementedError()

    def validate(self, table):
        """
        Perform any checks necessary to verify this computation can run on the
        provided table without errors. This is called by :meth:`.Table.compute`
        before :meth:`run`.
        """
        pass

    def run(self, table):
        """
        When invoked with a table, returns a sequence of new column values.
        """
        raise NotImplementedError()
