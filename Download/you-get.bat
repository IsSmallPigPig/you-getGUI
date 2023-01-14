rem -*- coding:gbk; mode:batch -*-
@echo off
cls

rem brief : install you-get & python on windows
rem author : gongqijian@gmail.com
rem date : 2013/03/04

rem ===========================================================

set ygroot=%~dp0
set ygroot=%ygroot:~0,-1%
set ygsrc=%ygroot%\you-get

set pyver=3.3.0
set pymsi=python-%pyver%.msi
set pydir=C:\Python33

rem ===========================================================

if /i "%PROCESSOR_IDENTIFIER:~0,3%" NEQ "X86" pymsi=python-%pyver%.amd64.msi

if not exist %pydir% (
    if not exist %pymsi% (
        wget.exe -c http://www.python.org/ftp/python/%pyver%/%pymsi%
	)
	echo ���ڰ�װ�����Ժ򡣡��� && msiexec.exe /i %pymsi% /qn
)

if not exist %ygsrc% (
    if not exist you-get.zip (
        wget.exe -O you-get.zip https://github.com/soimort/you-get/archive/master.zip
	)
	7za.exe x you-get.zip -o"%ygsrc%"
)

if not exist get.cmd echo python you-get/you-get-master/you-get %%*>get.cmd

rem ===========================================================

set PATH=%PATH%;%pydir%;%ygsrc%/you-get-master

cls
color 27

echo usage:
echo.
echo    get [url]
echo.
echo example:
echo.
echo    get www.youtube.com/watch?v=jNQXAC9IVRw
echo.
echo * ע�⿴�ϱߵ����ӣ�
echo * ������Ƶ���ز��ˣ�
echo * ճ����ʹ������Ҽ������� ctrl + v �ɡ�
echo * ��ֹ�����밴 ctrl + c ������ֱ�Ӳ�����ڡ�
echo * ���ж�أ�ɾ�� %pydir% Ŀ¼���ɣ���ȫ�޶������á�

cmd /k "cd %ygroot%"
