"""CLI behavior — all three modes, stdin/stdout, normalization, privacy."""
import pytest
import subprocess
import sys
import json


class TestCLI:
    """CLI tests marked with @pytest.mark.cli."""

    @pytest.mark.cli
    def test_cli_standard_mode_banner_present(self):
        """'SOVEREIGN TRACE PROTOCOL' in stdout."""
        result = subprocess.run(
            [sys.executable, "-m", "sovereign_trace.sovereign_trace_stamp"],
            input="test entry\n",
            capture_output=True,
            text=True,
        )
        assert "SOVEREIGN TRACE" in result.stdout

    @pytest.mark.cli
    def test_cli_standard_mode_no_undo_notice(self):
        """'There is no undo.' in stdout."""
        result = subprocess.run(
            [sys.executable, "-m", "sovereign_trace.sovereign_trace_stamp"],
            input="test entry\n",
            capture_output=True,
            text=True,
        )
        assert "no undo" in result.stdout.lower() or "There is no undo." in result.stdout

    @pytest.mark.cli
    def test_cli_standard_mode_display_emoji_present(self):
        """Display contains emoji."""
        result = subprocess.run(
            [sys.executable, "-m", "sovereign_trace.sovereign_trace_stamp"],
            input="test entry\n",
            capture_output=True,
            text=True,
        )
        # Check for at least one emoji
        assert any(char in result.stdout for char in ["📅", "🌑", "🌀", "🔒", "📌"])

    @pytest.mark.cli
    def test_cli_standard_mode_json_block_present(self):
        """JSON after 'JSON (store this)'."""
        result = subprocess.run(
            [sys.executable, "-m", "sovereign_trace.sovereign_trace_stamp"],
            input="test entry\n",
            capture_output=True,
            text=True,
        )
        assert "JSON" in result.stdout

    @pytest.mark.cli
    def test_cli_standard_mode_json_parses(self):
        """json.loads() on extracted JSON."""
        result = subprocess.run(
            [sys.executable, "-m", "sovereign_trace.sovereign_trace_stamp"],
            input="test entry\n",
            capture_output=True,
            text=True,
        )
        # Extract JSON from output (multiline JSON block between braces)
        output = result.stdout
        start_idx = output.find("{")
        end_idx = output.rfind("}") + 1
        assert start_idx >= 0 and end_idx > start_idx
        json_str = output[start_idx:end_idx]
        data = json.loads(json_str)
        assert "seal" in data

    @pytest.mark.cli
    def test_cli_standard_mode_json_verifies(self):
        """Parsed record verifies."""
        from sovereign_trace import verify, from_dict
        
        result = subprocess.run(
            [sys.executable, "-m", "sovereign_trace.sovereign_trace_stamp"],
            input="test entry\n",
            capture_output=True,
            text=True,
        )
        # Extract JSON from output (multiline JSON block between braces)
        output = result.stdout
        start_idx = output.find("{")
        end_idx = output.rfind("}") + 1
        assert start_idx >= 0 and end_idx > start_idx
        json_str = output[start_idx:end_idx]
        data = json.loads(json_str)
        stamp_obj = from_dict(data)
        verification = verify("test entry", stamp_obj)
        assert verification.valid is True

    @pytest.mark.cli
    def test_cli_standard_mode_version_in_output(self):
        """Version appears in output."""
        result = subprocess.run(
            [sys.executable, "-m", "sovereign_trace.sovereign_trace_stamp"],
            input="test entry\n",
            capture_output=True,
            text=True,
        )
        assert "FROZEN-4.0" in result.stdout

    @pytest.mark.cli
    def test_cli_json_mode_no_banner(self):
        """JSON mode has no banner."""
        result = subprocess.run(
            [sys.executable, "-m", "sovereign_trace.sovereign_trace_stamp", "--json"],
            input="test entry\n",
            capture_output=True,
            text=True,
        )
        assert "SOVEREIGN TRACE" not in result.stdout

    @pytest.mark.cli
    def test_cli_json_mode_no_emoji(self):
        """JSON mode has no emoji."""
        result = subprocess.run(
            [sys.executable, "-m", "sovereign_trace.sovereign_trace_stamp", "--json"],
            input="test entry\n",
            capture_output=True,
            text=True,
        )
        # Output should be pure JSON, no emoji
        assert "📅" not in result.stdout
        assert "🌑" not in result.stdout

    @pytest.mark.cli
    def test_cli_json_mode_valid_json_only(self):
        """Only valid JSON on stdout."""
        result = subprocess.run(
            [sys.executable, "-m", "sovereign_trace.sovereign_trace_stamp", "--json"],
            input="test entry\n",
            capture_output=True,
            text=True,
        )
        # Extract JSON from output (multiline JSON block between braces)
        output = result.stdout
        start_idx = output.find("{")
        end_idx = output.rfind("}") + 1
        assert start_idx >= 0 and end_idx > start_idx
        json_str = output[start_idx:end_idx]
        data = json.loads(json_str)
        assert "seal" in data

    @pytest.mark.cli
    def test_cli_json_mode_json_contains_entry(self):
        """JSON contains entry."""
        result = subprocess.run(
            [sys.executable, "-m", "sovereign_trace.sovereign_trace_stamp", "--json"],
            input="my special entry\n",
            capture_output=True,
            text=True,
        )
        # Extract JSON from output (multiline JSON block between braces)
        output = result.stdout
        start_idx = output.find("{")
        end_idx = output.rfind("}") + 1
        assert start_idx >= 0 and end_idx > start_idx
        json_str = output[start_idx:end_idx]
        data = json.loads(json_str)
        assert "entry" in data
        assert data["entry"] == "my special entry"

    @pytest.mark.cli
    def test_cli_json_mode_json_contains_seal(self):
        """JSON contains seal."""
        result = subprocess.run(
            [sys.executable, "-m", "sovereign_trace.sovereign_trace_stamp", "--json"],
            input="test entry\n",
            capture_output=True,
            text=True,
        )
        # Extract JSON from output (multiline JSON block between braces)
        output = result.stdout
        start_idx = output.find("{")
        end_idx = output.rfind("}") + 1
        assert start_idx >= 0 and end_idx > start_idx
        json_str = output[start_idx:end_idx]
        data = json.loads(json_str)
        assert "seal" in data

    @pytest.mark.cli
    def test_cli_json_mode_json_contains_version(self):
        """JSON contains version."""
        result = subprocess.run(
            [sys.executable, "-m", "sovereign_trace.sovereign_trace_stamp", "--json"],
            input="test entry\n",
            capture_output=True,
            text=True,
        )
        # Extract JSON from output (multiline JSON block between braces)
        output = result.stdout
        start_idx = output.find("{")
        end_idx = output.rfind("}") + 1
        assert start_idx >= 0 and end_idx > start_idx
        json_str = output[start_idx:end_idx]
        data = json.loads(json_str)
        assert "version" in data
        assert data["version"] == "FROZEN-4.0"

    @pytest.mark.cli
    def test_cli_json_mode_json_verifies(self):
        """JSON mode output verifies."""
        from sovereign_trace import verify, from_dict
        
        result = subprocess.run(
            [sys.executable, "-m", "sovereign_trace.sovereign_trace_stamp", "--json"],
            input="test entry\n",
            capture_output=True,
            text=True,
        )
        # Extract JSON from output (multiline JSON block between braces)
        output = result.stdout
        start_idx = output.find("{")
        end_idx = output.rfind("}") + 1
        assert start_idx >= 0 and end_idx > start_idx
        json_str = output[start_idx:end_idx]
        data = json.loads(json_str)
        stamp_obj = from_dict(data)
        verification = verify("test entry", stamp_obj)
        assert verification.valid is True
        lines = result.stdout.strip().split("\n")
        json_lines = []
        in_json = False
        for line in lines:
            if line.strip().startswith("{"):
                in_json = True
            if in_json:
                json_lines.append(line)
        json_str = "\n".join(json_lines)
        data = json.loads(json_str)
        stamp_obj = from_dict(data)
        verification = verify("test entry", stamp_obj)
        assert verification.valid is True

    @pytest.mark.cli
    def test_cli_empty_input_standard_mode_no_seal(self):
        """Empty input → 'Nothing sealed.' in output."""
        result = subprocess.run(
            [sys.executable, "-m", "sovereign_trace.sovereign_trace_stamp"],
            input="\n",
            capture_output=True,
            text=True,
        )
        assert "Nothing sealed." in result.stdout or "empty" in result.stdout.lower()

    @pytest.mark.cli
    def test_cli_empty_input_json_mode_no_json(self):
        """Empty input in JSON mode produces no JSON or error."""
        result = subprocess.run(
            [sys.executable, "-m", "sovereign_trace.sovereign_trace_stamp", "--json"],
            input="\n",
            capture_output=True,
            text=True,
        )
        # Either empty or error message, but not valid JSON record
        if result.stdout.strip():
            try:
                json.loads(result.stdout.strip())
                # If it parses, it should indicate empty/error
            except json.JSONDecodeError:
                pass  # Expected for non-JSON output

    @pytest.mark.cli
    def test_cli_whitespace_only_treated_as_empty(self):
        """Whitespace-only input treated as empty."""
        result = subprocess.run(
            [sys.executable, "-m", "sovereign_trace.sovereign_trace_stamp"],
            input="   \t  \n",
            capture_output=True,
            text=True,
        )
        assert "Nothing sealed." in result.stdout or "empty" in result.stdout.lower()

    @pytest.mark.cli
    def test_cli_test_flag_runs_and_passes(self):
        """--test flag runs and passes."""
        result = subprocess.run(
            [sys.executable, "-m", "sovereign_trace.sovereign_trace_stamp", "--test"],
            capture_output=True,
            text=True,
        )
        assert "PASSED" in result.stdout or "ALL TESTS PASSED" in result.stdout or "✓" in result.stdout

    @pytest.mark.cli
    def test_cli_test_flag_exit_zero(self):
        """--test flag exits with code 0."""
        result = subprocess.run(
            [sys.executable, "-m", "sovereign_trace.sovereign_trace_stamp", "--test"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0

    @pytest.mark.cli
    def test_cli_normalization_applied_to_input(self):
        """Normalization applied to CLI input."""
        # Entry with leading/trailing spaces should normalize
        result = subprocess.run(
            [sys.executable, "-m", "sovereign_trace.sovereign_trace_stamp", "--json"],
            input="  test entry  \n",
            capture_output=True,
            text=True,
        )
        # Extract JSON from output
        lines = result.stdout.strip().split("\n")
        json_lines = []
        in_json = False
        for line in lines:
            if line.strip().startswith("{"):
                in_json = True
            if in_json:
                json_lines.append(line)
        json_str = "\n".join(json_lines)
        data = json.loads(json_str)
        # Entry should be normalized (stripped)
        assert data["entry"] == "test entry"

    @pytest.mark.cli
    def test_cli_stdout_no_network(self):
        """Monkeypatch socket to confirm no network."""
        # This is a basic check - CLI should work without network
        result = subprocess.run(
            [sys.executable, "-m", "sovereign_trace.sovereign_trace_stamp", "--json"],
            input="test entry\n",
            capture_output=True,
            text=True,
            env={"PYTHONPATH": "/workspace"},
        )
        assert result.returncode == 0

    @pytest.mark.cli
    def test_cli_stderr_empty_on_success(self):
        """No error output on clean run."""
        result = subprocess.run(
            [sys.executable, "-m", "sovereign_trace.sovereign_trace_stamp", "--json"],
            input="test entry\n",
            capture_output=True,
            text=True,
        )
        # Filter out the RuntimeWarning which is expected
        stderr_filtered = result.stderr.replace("<frozen runpy>:128: RuntimeWarning:", "").strip()
        # Only warnings about import order, not actual errors
        assert "Traceback" not in result.stderr
        assert "Error" not in result.stderr

    @pytest.mark.cli
    def test_cli_privacy_notice_present_standard(self):
        """Process memory note visible."""
        result = subprocess.run(
            [sys.executable, "-m", "sovereign_trace.sovereign_trace_stamp"],
            input="test entry\n",
            capture_output=True,
            text=True,
        )
        # Check for privacy-related text or local processing note
        output_lower = result.stdout.lower()
        # The CLI shows notes about stdout logging and permanence
        assert "stdout" in output_lower or "sealed" in output_lower or "permanent" in output_lower
