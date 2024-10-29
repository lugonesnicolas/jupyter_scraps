docker run --interactive --tty ^
 --name beon-jupyter-dev ^
 --volume "%CD%":/workdir ^
 --env-file .env ^
 --publish 8888:8888 ^
 %* ^
 beon-jupyter:0.0.1 ^
 bash