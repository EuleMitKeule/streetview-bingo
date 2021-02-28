import { Component, OnInit, Output, EventEmitter, Input } from '@angular/core';
import { DefaultService, Hello } from 'generated/openapi';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-hello',
  templateUrl: './hello.component.html',
  styleUrls: ['./hello.component.css']
})
export class HelloComponent implements OnInit {

  hello$: Observable<Hello[]>;

  @Output() clickedButton = new EventEmitter<string>();
  @Input() text;

  constructor(private defaultService: DefaultService) { }

  ngOnInit(): void {
    this.hello$ = this.defaultService.apiHello();
  }

  test(): void {
    this.clickedButton.emit("test123");
  }

}
