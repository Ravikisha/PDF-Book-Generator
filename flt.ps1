Copy-Item  -Path "./logos" -Destination "./pdf_book/android/app/src/main/res" -Recurse -force
echo "Copy Logo"
python index.py
cd pdf_book
flutter build apk --release
echo "Build Complete."
cd..
echo "Build Complete next cd"
Copy-Item ".\pdf_book\build\app\outputs\apk\release\app-release.apk" -Destination ".\release"
echo "copy completed"