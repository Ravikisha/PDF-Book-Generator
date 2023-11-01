xcopy /s "./logos" "./pdf_book/android/app/src/main/res" /Y
python index.py
cd pdf_book
flutter build apk --release
echo "Build Complete."
cd..
echo "Build Complete next cd"
copy .\pdf_book\build\app\outputs\apk\release\app-release.apk .\release