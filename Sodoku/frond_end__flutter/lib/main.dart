import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(title: 'Sodoku', home: SodokuInput());
  }
}

class SodokuInput extends StatefulWidget {
  @override
  _SodokuInputState createState() => _SodokuInputState();
}

class _SodokuInputState extends State<SodokuInput> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Sodoku Solver'),
      ),
      body: mainWidget(),
    );
  }
}

var values = List.generate(9, (i) => List.generate(9, (j) => 0));
var beispiel = values[0][0];

mainWidget() {
  return sodoku();
}

Future<http.Response> gameBoard(List<List<int>> feld) async {
  final url = Uri.http("0.0.0.0:5000", "/");

  final resp = await http.post(url, body: {"feld": jsonEncode(feld)});

  final String respString = resp.body;
  return resp;
}

Future<http.Response> testRequest() async {
  final url = Uri.http("192.168.178.76", "/piapp", {"status": "turnOn"});

  final resp = await http.get(url);

  return resp;
}

Widget sodoku() {
  return Column(
    children: [
      Container(
          child: Column(
        children: _buildfeld(9),
      )),
      Text('Hallo'),
      ElevatedButton(
          onPressed: () async {
            final resp = await gameBoard(values);
            print(resp);
          },
          child: Text('Submit')),
      ElevatedButton(
          onPressed: () async {
            final response = await testRequest();
            print(response);
          },
          child: Text('Test'))
    ],
  );
}

List<Widget> _buildfeld(int i) => List.generate(
      i,
      (index) {
        return Row(
          children: _buildfeldRow(i, index),
        );
      },
    );

List<Widget> _buildfeldRow(int i, int n) => List.generate(i, (index) {
      return Container(
        child: TextField(
          onChanged: (value) {
            values[n][index] = int.parse(value);
            for (var c = 0; c < 9; c++) {
              print(values[c]);
            }
          },
          decoration: InputDecoration(
              counterText: '', contentPadding: EdgeInsets.all(10.0)),
          textAlign: TextAlign.center,
          textAlignVertical: TextAlignVertical.center,
          maxLength: 1,
          keyboardType: TextInputType.number,
          //style: TextStyle(fontSize: 40),
        ),
        decoration: BoxDecoration(
          border: Border.all(color: Colors.black),
        ),
        width: 40,
        height: 40,
      );
    });
