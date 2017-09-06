@echo off

set html5Dir=%cd%\..\html5_master
set destDir=%cd%\..\Sperry\src\app\components\sperry\js\geotoolkit

set debugSource="%html5Dir%\bin"
set advSource="%html5Dir%\GeoToolkitJS\lib\bin"
set tsSource="%html5Dir%\GeoToolkitJS\lib\bin\headers\typescript"

set list=geotoolkit geotoolkit.controls geotoolkit.crosssection geotoolkit.data geotoolkit.map geotoolkit.pdf geotoolkit.svg geotoolkit.welllog geotoolkit.welllog.las geotoolkit.welllog.widgets geotoolkit.widgets geotoolkit.seismic

echo Copying files...
for %%f in (%list%) do (
    
	echo.
	echo Copying %%f.adv.js
    copy %advSource%\%%f.adv.js %destDir% /Y

	echo.
	echo Copying %%f.js
	copy %debugSource%\%%f.js %destDir% /Y

	echo.
	echo copying %%f.d.ts
	copy %tsSource%\%%f.d.ts %destDir%\headers /Y	
)
