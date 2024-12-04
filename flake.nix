{
  description = "Advent of Code";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    let
      systems = with flake-utils.lib; [
        system."x86_64-linux"
        system."aarch64-darwin"
      ];
    in 
      flake-utils.lib.eachSystem systems (system: 
        let
          pkgs = import nixpkgs {
            inherit system;
            config = {
              allowUnfree = true;
              allowUnfreePredicate = (_: true);
            };
          };

        in {
          devShells.default = pkgs.mkShell {
            buildInputs = with pkgs; [
              python3
            ];

            shellHook = ''
		      VENV=./python/venv;
      		  if test ! -d $VENV; then
        	    python -m venv $VENV;
      		  fi
      		  source ./$VENV/bin/activate;
		      export PYTHONPATH="$VENV/lib/python3.12/site-packages:."
            '';
          };
        });
}
