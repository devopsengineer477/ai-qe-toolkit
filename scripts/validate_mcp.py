from pathlib import Path
import json, sys

ROOT = Path(__file__).resolve().parents[1]
FILES = [
    "integrations/mcp/templates/claude-code/.mcp.json",
    "integrations/mcp/templates/vscode/mcp.json",
    "integrations/mcp/templates/copilot-portable/.mcp.json",
    "integrations/mcp/policy/mcp-policy.json",
    "integrations/mcp/contracts/provider-capabilities.json",
]
FORBIDDEN = ["ghp_", "github_pat_", "xoxb-", "sk-ant-", "BEGIN PRIVATE KEY"]

def load(rel):
    path = ROOT / rel
    if not path.is_file():
        raise FileNotFoundError(rel)
    raw = path.read_text(encoding="utf-8")
    for marker in FORBIDDEN:
        if marker in raw:
            raise ValueError(f"Possible credential material found in {rel}")
    return json.loads(raw)

def main():
    errors = []
    configs = {}
    for rel in FILES:
        try:
            configs[rel] = load(rel)
        except Exception as exc:
            errors.append(f"{rel}: {exc}")
    for rel, config in configs.items():
        if "templates/claude-code" in rel or "templates/copilot-portable" in rel:
            servers = config.get("mcpServers", {})
        elif "templates/vscode" in rel:
            servers = config.get("servers", {})
        else:
            continue
        for name in ("atlassian", "github"):
            if name not in servers:
                errors.append(f"{rel}: missing {name} server")
        github = servers.get("github", {})
        if github.get("headers", {}).get("X-MCP-Readonly") != "true":
            errors.append(f"{rel}: GitHub server must stay read-only")
        if "jenkins" in servers:
            headers = servers["jenkins"].get("headers", {})
            if "JENKINS_MCP_BASIC_AUTH" not in headers.get("Authorization", ""):
                errors.append(f"{rel}: Jenkins auth must use external environment variable")
    if errors:
        print("MCP validation FAILED:\\n" + "\\n".join(" - " + e for e in errors))
        return 1
    print(f"MCP validation PASSED: {len(FILES)} JSON files parsed; client templates and safe defaults checked.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
