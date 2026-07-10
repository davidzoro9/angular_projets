import { Component, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { WeatherComponent } from './components/weather/weather';
import { KanbanComponent } from './components/kanban/kanban';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, WeatherComponent, KanbanComponent],
  templateUrl: './app.html',
  styleUrl: './app.scss'
})
export class App {
  title = 'Angular Advanced Projects';
  activeTab = signal<'weather' | 'kanban'>('weather');

  setTab(tab: 'weather' | 'kanban'): void {
    this.activeTab.set(tab);
  }
}
