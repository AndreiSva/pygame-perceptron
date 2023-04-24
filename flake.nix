{
  description = "A flake for building pygame-perceptron";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system}; in
      {
        packages = rec {
          Damnation = pkgs.python311Packages.buildPythonPackage rec {
            name = "perceptron";
            format = "pyproject";
            src = ./.;
            propagatedBuildInputs = with pkgs.python311Packages; [
              setuptools
              pygame
              numpy
            ];
          };
          default = Damnation;
        };

        apps = rec {
          game_app = flake-utils.lib.mkApp {
            drv = self.packages.${system}.Damnation;
            name = "perceptron";
          };
          default = game_app;
        };
        
      }
    );
}
