…or create a new repository on the command line
echo "# pytest_practices1" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/790212828/pytest_practices1.git
git push -u origin main

…or push an existing repository from the command line
git remote add origin https://github.com/790212828/pytest_practices1.git
git branch -M main
git push -u origin main



"""
生成allure-report命令：
cmd:cd .py文件路径下
pytest --clean --alluredir=./result/2/ test_homework.py
allure generate ./result/2/ -o ./report/2/
allure open -h 127.0.0.1 -p 8090 ./report/2/
"""
