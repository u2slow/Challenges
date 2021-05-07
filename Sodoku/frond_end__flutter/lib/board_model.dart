// To parse this JSON data, do
//
//     final board = boardFromJson(jsonString);

import 'dart:convert';

Board boardFromJson(String str) => Board.fromJson(json.decode(str));

String boardToJson(Board data) => json.encode(data.toJson());

class Board {
  Board({
    this.message,
    this.feld,
  });

  String message;
  List<List<int>> feld;

  factory Board.fromJson(Map<String, dynamic> json) => Board(
        message: json["message"],
        feld: List<List<int>>.from(
            json["Feld"].map((x) => List<int>.from(x.map((x) => x)))),
      );

  Map<String, dynamic> toJson() => {
        "message": message,
        "Feld": List<dynamic>.from(
            feld.map((x) => List<dynamic>.from(x.map((x) => x)))),
      };
}
