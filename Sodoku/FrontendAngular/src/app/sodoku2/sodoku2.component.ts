import { Component, OnInit } from '@angular/core';
import { HttpClient} from '@angular/common/http'

@Component({
  selector: 'app-sodoku2',
  templateUrl: './sodoku2.component.html',
  styleUrls: ['./sodoku2.component.css']
})
export class Sodoku2Component implements OnInit {
  constructor(private http: HttpClient) { }

  ngOnInit() {
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
    const button = document.createElement('button')
    button.addEventListener('click', this.solve)
    button.innerHTML = "Solve";
    document.getElementById('Sodoku').appendChild(button)
  }

  solve (){
    this.http.get('http://127.0.0.1:5000/test', ).toPromise().then(data => {
      console.log(data)
    })
  }
}
