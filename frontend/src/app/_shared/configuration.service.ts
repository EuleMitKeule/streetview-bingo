import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ConfigurationService {

  private config: any;

  constructor(private http: HttpClient) { }

  public loadConfig() {
    return this.http.get('./assets/config/config.json')
      .toPromise()
      .then((config: any) => {
        this.config = config;
        console.log(this.config);
      })
      .catch((err: any) => {
        console.error(err);
      });
  }

  getConfig() {
    return this.config;
  }

}
