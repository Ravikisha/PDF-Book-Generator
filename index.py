import os
app_name = input("Enter the app name : ")
file_name = input("Enter the file name(pdf file): ")

writedatamain = '''
import 'package:flutter/material.dart';
import 'package:native_pdf_view/native_pdf_view.dart';

void main() => runApp(MyApp());

class MyApp extends StatefulWidget {
  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  static final int _initialPage = 1;
  int _actualPageNumber = _initialPage, _allPagesCount = 0;
  bool isSampleDoc = true;
  late PdfController _pdfController;

  @override
  void initState() {
    _pdfController = PdfController(
      document: PdfDocument.openAsset('assets/%s'),
      initialPage: _initialPage,
    );
    super.initState();
  }

  @override
  void dispose() {
    _pdfController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) => MaterialApp(
        theme: ThemeData(primaryColor: Colors.black),
        home: Scaffold(
          appBar: AppBar(
            title: Text('%s'),
            actions: <Widget>[
              IconButton(
                icon: Icon(Icons.navigate_before),
                onPressed: () {
                  _pdfController.previousPage(
                    curve: Curves.ease,
                    duration: Duration(milliseconds: 100),
                  );
                },
              ),
              Container(
                alignment: Alignment.center,
                child: Text(
                  '$_actualPageNumber/$_allPagesCount',
                  style: TextStyle(fontSize: 22),
                ),
              ),
              IconButton(
                icon: Icon(Icons.navigate_next),
                onPressed: () {
                  _pdfController.nextPage(
                    curve: Curves.ease,
                    duration: Duration(milliseconds: 100),
                  );
                },
              ),
            ],
          ),
          body: PdfView(
            documentLoader: Center(child: CircularProgressIndicator()),
            pageLoader: Center(child: CircularProgressIndicator()),
            controller: _pdfController,
            onDocumentLoaded: (document) {
              setState(() {
                _allPagesCount = document.pagesCount;
              });
            },
            onPageChanged: (page) {
              setState(() {
                _actualPageNumber = page;
              });
            },
          ),
        ),
      );
}
''' % (file_name,app_name)

writedatamainfest = '''
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.pdf_book">
   <application
        android:label="%s"
        android:icon="@mipmap/ic_launcher">
        <activity
            android:name=".MainActivity"
            android:launchMode="singleTop"
            android:theme="@style/LaunchTheme"
            android:configChanges="orientation|keyboardHidden|keyboard|screenSize|smallestScreenSize|locale|layoutDirection|fontScale|screenLayout|density|uiMode"
            android:hardwareAccelerated="true"
            android:windowSoftInputMode="adjustResize">
            <!-- Specifies an Android theme to apply to this Activity as soon as
                 the Android process has started. This theme is visible to the user
                 while the Flutter UI initializes. After that, this theme continues
                 to determine the Window background behind the Flutter UI. -->
            <meta-data
              android:name="io.flutter.embedding.android.NormalTheme"
              android:resource="@style/NormalTheme"
              />
            <!-- Displays an Android View that continues showing the launch screen
                 Drawable until Flutter paints its first frame, then this splash
                 screen fades out. A splash screen is useful to avoid any visual
                 gap between the end of Android's launch screen and the painting of
                 Flutter's first frame. -->
            <meta-data
              android:name="io.flutter.embedding.android.SplashScreenDrawable"
              android:resource="@drawable/launch_background"
              />
            <intent-filter>
                <action android:name="android.intent.action.MAIN"/>
                <category android:name="android.intent.category.LAUNCHER"/>
            </intent-filter>
        </activity>
        <!-- Don't delete the meta-data below.
             This is used by the Flutter tool to generate GeneratedPluginRegistrant.java -->
        <meta-data
            android:name="flutterEmbedding"
            android:value="2" />
    </application>
</manifest>
''' % (app_name)

with open("./pdf_book/lib/main.dart", "w") as file:
    file.write(writedatamain)

#read file
with open("./pdf_book/android/app/src/main/AndroidManifest.xml", "w") as file:
    file.write(writedatamainfest)
