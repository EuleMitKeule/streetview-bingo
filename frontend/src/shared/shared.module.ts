import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { UserBadgeComponent } from './user-badge/user-badge.component';
import { WordBadgeComponent } from './word-badge/word-badge.component';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';


@NgModule({
  declarations: [
    UserBadgeComponent,
    WordBadgeComponent
  ],
  imports: [
    CommonModule,
    FontAwesomeModule
  ],
  exports: [
    UserBadgeComponent,
    WordBadgeComponent,
  ]
})
export class SharedModule { }
