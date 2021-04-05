import { element } from 'protractor';
import { GetApiService } from './../get-api.service';
import { HttpClient} from '@angular/common/http';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-sodoku',
  templateUrl: './sodoku.component.html',
  styleUrls: ['./sodoku.component.css']
})
export class SodokuComponent implements OnInit {
  feld = []
  public constructor(private http: HttpClient) { }

  ngOnInit(): void {
    var solvButton = document.getElementById('solve')
    solvButton.style.visibility = "hidden";
    var solvButton = document.getElementById('reset')
    solvButton.style.visibility = "hidden";
  }

  createTable(){
    document.getElementById('start').remove();
    for (let i = 0; i < 9; i++){
      for (let k = 0; k < 9; k++){
        const elemet = document.getElementById('Sodoku');
        const id = String(i) + '/' + String(k);
        const input = document.createElement('input');
        input.type = "text";
        input.maxLength = 1;
        input.style.textAlign = "center";
        input.style.backgroundColor = "rgb(185,185,185)";
        input.style.width = "75px";
        input.style.height = "75px";
        input.style.fontSize = "75px";
        input.id = id;
        input.style.gridColumn = String(k+1)
        input.style.gridRow = String(i + 1);
        if (k == 3 || k == 6){
          input.style.borderLeft = "5px solid";
        }
        if (i == 3|| i == 6){
          input.style.borderTop = "5px solid";
        }
        //newElement.appendChild(input)
        elemet.appendChild(input);
      }
    }
    //hier soll der solve button sichtbar gemacht werden
    var soButton = document.getElementById('solve')
    soButton.style.visibility = "visible";
    var soButton = document.getElementById('reset')
    soButton.style.visibility = "visible";
  }
  solve(): void{
    var copyFeld = []
    for(let i = 0; i < 9; i++){
      copyFeld.push([])
      for(let k = 0; k < 9; k++){
        var cellvalaue = (<HTMLInputElement>document.getElementById(String(i)+ "/"+ String(k))).value;
        if (cellvalaue == undefined){
          copyFeld[i].push(0)
        }
        else{
          copyFeld[i].push(Number(cellvalaue))
        }
      }
    }
    console.log(copyFeld)
    this.feld = copyFeld
    this.http.post('http://127.0.0.1:5000/',copyFeld).toPromise().then(data =>{
      console.log(data['Feld'])
      this.feld = data['Feld'];
      this.updateFeld()
    })
  }
  updateFeld(){
    for (let i = 0; i < 9; i++){
      for (let n = 0; n< 9; n++){
        (<HTMLInputElement>document.getElementById(String(i)+ "/"+ String(n))).value =this.feld[i][n];
      }
    }
  }
  resetFeld(){
    for (let i = 0; i < 9; i++){
      for (let n = 0; n< 9; n++){
        this.feld[i][n] = ""
      }
    }
    this.updateFeld()
  }
}
