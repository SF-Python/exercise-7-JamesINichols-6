import re

from exercise7 import generate_hex_digits

import unittest

class HexDigits(unittest.TestCase):
    MAC_REGEX = re.compile(r"^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$")

    def generateMACAddress(self):
        return generate_hex_digits()

    def is_valid_mac(self, mac: str) -> bool:
        """Check format and hex correctness."""
        return bool(HexDigits.MAC_REGEX.match(mac))

    def check_randomness(self,samples=10):
        """Ensure the MAC generator produces different values."""
        generated = {self.generateMACAddress() for _ in range(samples)}
        return len(generated) == samples, generated


    def test_mac_generator(self):
        """Runs a series of tests against the MAC generator."""
        results = {}

        # 1. Test single output formatting
        mac = self.generateMACAddress()
        results["sample_mac"] = mac
        results["format_valid"] = self.is_valid_mac(mac)

        # 2. Check randomness
        is_random, sample_set = self.check_randomness()
        results["randomness_valid"] = is_random
        results["sample_set"] = sample_set

        print("=== MAC Generator Test Report ===")
        print(f"Sample MAC generated:          {results['sample_mac']}")
        print(f"Valid MAC format:              {results['format_valid']}")
        print(f"Randomness (10 unique tests):  {results['randomness_valid']}")
        print("Generated set:")
        for item in results["sample_set"]:
            print("  ", item)


if __name__ == "__main__":
    unittest.main()