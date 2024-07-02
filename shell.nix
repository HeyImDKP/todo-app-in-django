{ pkgs ? import <nixpkgs> }: pkgs.mkShell {
    nativeBuildInputs = (with pkgs; [ 
        python312 
    ]) ++ (with pkgs.python312Packages; [
        django
    ]);
}