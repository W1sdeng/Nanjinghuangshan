import 'package:flutter_test/flutter_test.dart';
import 'package:yicun/main.dart';

void main() {
  testWidgets('App should render welcome text', (tester) async {
    await tester.pumpWidget(const YicunApp());
    expect(find.text('进一寸，有一寸的欢喜。'), findsOneWidget);
  });
}
