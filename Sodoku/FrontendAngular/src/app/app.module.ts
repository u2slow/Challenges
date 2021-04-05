import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SodokuComponent } from './sodoku/sodoku.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { Sodoku2Component } from './sodoku2/sodoku2.component';


@NgModule({
  declarations: [
    AppComponent,
    SodokuComponent,
    Sodoku2Component
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    BrowserAnimationsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
