import { Component, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

interface Task {
  id: string;
  title: string;
  category: string;
  status: 'todo' | 'in_progress' | 'done';
}

@Component({
  selector: 'app-kanban',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './kanban.html',
  styleUrl: './kanban.scss'
})
export class KanbanComponent {
  // Utilizing Angular Signals for modern state management (Angular 17+)
  tasks = signal<Task[]>([
    { id: '1', title: 'Implement Stripe Elements Checkout Flow', category: 'Backend', status: 'todo' },
    { id: '2', title: 'Write unit tests for Odoo MRP scheduler', category: 'Testing', status: 'in_progress' },
    { id: '3', title: 'Design responsive weather search component', category: 'Frontend', status: 'done' },
    { id: '4', title: 'Configure Kubernetes session cache using Redis', category: 'DevOps', status: 'todo' }
  ]);

  newTaskTitle = '';
  newTaskCategory = 'Frontend';
  draggedTaskId: string | null = null;

  // Columns specification
  columns: { key: 'todo' | 'in_progress' | 'done'; title: string }[] = [
    { key: 'todo', title: 'To Do' },
    { key: 'in_progress', title: 'In Progress' },
    { key: 'done', title: 'Done' }
  ];

  getTasksByStatus(status: 'todo' | 'in_progress' | 'done') {
    return this.tasks().filter(t => t.status === status);
  }

  addTask(): void {
    if (!this.newTaskTitle.trim()) return;

    const newTask: Task = {
      id: Date.now().toString(),
      title: this.newTaskTitle.trim(),
      category: this.newTaskCategory,
      status: 'todo'
    };

    // Update list using signal setter
    this.tasks.update(current => [...current, newTask]);
    this.newTaskTitle = ''; // Reset input
  }

  deleteTask(id: string): void {
    this.tasks.update(current => current.filter(t => t.id !== id));
  }

  // --- DRAG & DROP NATIVE API HANDLERS ---
  onDragStart(taskId: string): void {
    this.draggedTaskId = taskId;
  }

  onDragOver(event: DragEvent): void {
    event.preventDefault(); // Required to allow drop
  }

  onDrop(status: 'todo' | 'in_progress' | 'done'): void {
    if (!this.draggedTaskId) return;

    this.tasks.update(current => 
      current.map(t => t.id === this.draggedTaskId ? { ...t, status } : t)
    );
    this.draggedTaskId = null; // Reset
  }
}
