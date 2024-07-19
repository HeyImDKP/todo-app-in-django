{ pkgs ? import <nixpkgs> }: pkgs.mkShell {
    nativeBuildInputs = (with pkgs; [ 
        python312
        nodejs_22
        typescript
    ]) ++ (with pkgs.python312Packages; [
        django
        djangorestframework
        django-cors-headers
    ]);
}
