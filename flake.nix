{
  description = "A very basic flake";

  inputs.nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";

  outputs =
    { self, nixpkgs }:
    let
      # Systems supported by this flake
      supportedSystems = [
        "x86_64-linux"
        "aarch64-linux"
        "x86_64-darwin"
        "aarch64-darwin"
      ];
      # A helper function for specifying per-system outputs
      forAllSystems =
        f:
        nixpkgs.lib.genAttrs supportedSystems (
          system:
          f nixpkgs.legacyPackages.${system}
        );
    in
    {
      # Development environments
      devShells = forAllSystems (
        pkgs:
        {
          default = pkgs.mkShell {
            packages = with pkgs; [
              # Add development environment packages here
              python311
              uv
            ];
          };
        }
      );

      # Package outputs
      packages = forAllSystems (
        pkgs:
        {
          # Build this by running `nix build`, `nix build .`, or `nix build .#default`
          # default = pkgs.hello;
        }
      );
    };
}
