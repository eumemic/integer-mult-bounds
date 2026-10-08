"""Controls for the annealed point-order witness."""
from fractions import Fraction as Q
from pathlib import Path
import importlib.util
import unittest

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT/'research/annealed-orders'
spec = importlib.util.spec_from_file_location('annealed_orders_witness', HERE/'witness.py')
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)


class AnnealedOrdersTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = w.run()

    def test_frozen_certificate(self):
        self.assertEqual(w.js(self.result), w.read(HERE/'certificate.json'))

    def test_strict_assembly_and_bracket(self):
        a = self.result['assembly']
        self.assertEqual(len(a['constraints']), 47)
        self.assertEqual(len(a['margins']), 7)
        self.assertTrue(all(x > 0 for x in a['constraints'].values()))
        self.assertGreater(w.KAPPA, w.PR47_KAPPA)
        self.assertGreater(w.KAPPA, Q(1, 2**15))
        self.assertLess(w.KAPPA, Q(1, 2**14))

    def test_fewer_roles_than_pr47(self):
        for h in (23, 25):
            ours = w.read(HERE/f'original-{h}.json')
            theirs = w.read(ROOT/f'research/climbed-producers/original-{h}.json')
            self.assertLess(ours['R'], theirs['R'])
            self.assertEqual(ours['loss'], theirs['loss'])

    def test_pr47_network_excluded(self):
        self.assertGreater(self.result['exclusion_lower_moments']['comparison-pr47.json'], 1)


if __name__ == '__main__':
    unittest.main()
