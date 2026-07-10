import { Component, OnInit, OnDestroy } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Subject, Observable, of } from 'rxjs';
import { debounceTime, distinctUntilChanged, switchMap, catchError, tap } from 'rxjs/operators';

interface WeatherData {
  city: string;
  temp: number;
  condition: string;
  humidity: number;
  wind: number;
  icon: string;
}

@Component({
  selector: 'app-weather',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './weather.html',
  styleUrl: './weather.scss'
})
export class WeatherComponent implements OnInit, OnDestroy {
  searchQuery = '';
  loading = false;
  errorMessage = '';
  
  // RxJS Subject for trigger search streams
  private searchSubject = new Subject<string>();
  
  // Observable for weather results
  weather$!: Observable<WeatherData | null>;

  // Mock Database for Weather
  private mockWeatherDb: { [key: string]: WeatherData } = {
    'paris': { city: 'Paris', temp: 22, condition: 'Sunny', humidity: 45, wind: 12, icon: '☀️' },
    'london': { city: 'London', temp: 16, condition: 'Rainy', humidity: 85, wind: 24, icon: '🌧️' },
    'ouagadougou': { city: 'Ouagadougou', temp: 35, condition: 'Hot & Sunny', humidity: 20, wind: 8, icon: '🔥' },
    'new york': { city: 'New York', temp: 20, condition: 'Cloudy', humidity: 60, wind: 15, icon: '☁️' },
    'tokyo': { city: 'Tokyo', temp: 18, condition: 'Windy', humidity: 55, wind: 30, icon: '💨' }
  };

  ngOnInit(): void {
    // Pipeline RxJS to handle auto-search with debounce and switchMap
    this.weather$ = this.searchSubject.pipe(
      debounceTime(400),
      distinctUntilChanged(),
      tap(() => {
        this.loading = true;
        this.errorMessage = '';
      }),
      switchMap(query => this.fetchWeather(query)),
      tap(() => this.loading = false)
    );
  }

  onSearchChange(value: string): void {
    this.searchSubject.next(value.toLowerCase().trim());
  }

  // Simulated API fetch
  private fetchWeather(query: string): Observable<WeatherData | null> {
    if (!query) {
      return of(null);
    }
    
    // Simulate web API delay and results
    return new Observable<WeatherData | null>(observer => {
      setTimeout(() => {
        const found = this.mockWeatherDb[query];
        if (found) {
          observer.next(found);
        } else {
          observer.error(new Error(`City "${query}" not found in our database.`));
        }
        observer.complete();
      }, 600);
    }).pipe(
      catchError(err => {
        this.errorMessage = err.message;
        return of(null);
      })
    );
  }

  ngOnDestroy(): void {
    // Unsubscribe and complete search stream to avoid memory leaks
    this.searchSubject.complete();
  }
}
