import json

class HarValidator:
    def __init__(self, har_file_path):
        with open(har_file_path, "r") as f:
            self.har = json.load(f)
        self.entries = self.har.get("log", {}).get("entries", [])

    def find_calls_to(self, endpoint_substring):
        return[
            e for e in self.entries
            if endpoint_substring in e["request"]["url"]
        ]

    def assert_status_code(self, entry, expected):
        actual = entry["response"]["status"]
        assert actual == expected, f"Expected {expected}, got {actual}"

    def assert_max_latency(self, entry, max_ms):
        timings = entry["timings"]
        total = sum(t for t in timings.values() if isinstance(t, (int,float)))
        assert total <= max_ms, f"Latency {total}ms exceeds {max_ms}ms"

    def assert_body_contains(self, entry, text):
        content = entry["response"].get("content", {}).get("text", "")
        assert text in content, f"'{text}' not found in response body"

    def run_sample_validations(self):
        print("Running HAR validations...")

        # Example: check login API calls
        login_calls = self.find_calls_to("/api/login")
        assert login_calls, "No calls found to /api/login"
        print(f"Found {len(login_calls)} login calls")

        # Validate status codes
        for call in login_calls:
            self.assert_status_code(call, 200)

        # Validate latency under 2 seconds
        for call in login_calls:
            self.assert_max_latency(call, 2000)

        # Validate response body contains expected field
        for call in login_calls:
            self.assert_body_contains(call, "token")

        print("✔ All HAR validations passed successfully!")

if __name__ == "__main__":
    validator = HarValidator("chatgpt.com.har")
    validator.run_sample_validations()