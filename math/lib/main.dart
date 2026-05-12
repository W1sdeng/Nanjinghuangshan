import 'package:flutter/material.dart';

void main() {
  runApp(const YicunApp());
}

class YicunApp extends StatelessWidget {
  const YicunApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: '一寸',
      debugShowCheckedModeBanner: false,
      home: const Scaffold(
        body: Center(
          child: Text('进一寸，有一寸的欢喜。'),
        ),
      ),
    );
  }
}
