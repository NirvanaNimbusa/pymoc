# Copyright (C) 2014 Science and Technology Facilities Council.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from unittest import TestCase

from pymoc import MOC

class OperatorsTestCase(TestCase):
    def test_iadd(self):
        p = MOC(4, (11, 12))
        p.add(5, (100,))

        q = MOC(4, (13,))
        q.add(5, (101,))

        p += q

        self.assertEqual(p.cells, 5)
        self.assertEqual(sorted(p[4]), [11, 12, 13])
        self.assertEqual(sorted(p[5]), [100, 101])

    def test_copy(self):
        # TODO: check metadata copying

        p = MOC(1, (2, 3))
        p.add(4, (5, 6))

        q = p.copy()

        self.assertEqual(q.cells, 4)
        self.assertEqual(sorted(q[1]), [2, 3])
        self.assertEqual(sorted(q[4]), [5, 6])

    def test_clear(self):
        p = MOC()
        p.add(4, (5, 6))
        p.add(0, (11,))
        p.add(1, (42, 43, 44))
        self.assertEqual(p.cells, 6)
        self.assertEqual(p.normalized, False)

        p.clear()
        self.assertEqual(p.cells, 0)
        self.assertEqual(p.normalized, True)

    def test_add(self):
        p = MOC(4, (11, 12))
        p.add(5, (100,))

        q = MOC(4, (13,))
        q.add(5, (101,))

        s = p + q

        # Check the original MOCs were not altered.
        self.assertEqual(p.cells, 3)
        self.assertEqual(q.cells, 2)

        # Check the sum is the union of p and q.
        self.assertEqual(s.cells, 5)
        self.assertEqual(sorted(s[4]), [11, 12, 13])
        self.assertEqual(sorted(s[5]), [100, 101])
