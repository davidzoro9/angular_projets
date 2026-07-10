# Angular Advanced Showcase: RxJS & Signals

This repository showcases advanced concepts in modern Angular development (v17+), featuring standalone components, reactive programming with RxJS, and clean state management using Angular Signals.

## 🚀 Projects Included

### 1. 🌦️ Reactive Weather Dashboard (RxJS Stream Pipeline)
A search-as-you-type weather dashboard demonstrating declarative reactive streams.
*   **RxJS Operators Used**:
    *   `debounceTime(400)`: Prevents spamming HTTP/API calls during typing.
    *   `distinctUntilChanged()`: Ensures requests are only sent if the search query actually changed.
    *   `tap()`: Handles side effects like triggering loaders and resetting errors.
    *   `switchMap()`: Cancels the previous pending HTTP/API requests if a new input is typed (avoids race conditions).
    *   `catchError()`: Gracefully intercepts errors and returns a fallback stream (`of(null)`) so the main observable doesn't terminate.
*   **Architecture**: Built entirely as a standalone component using the `async` pipe for automatic subscription management (zero memory leaks).

### 2. 📋 Signal-Driven Kanban Board (Angular Signals)
An interactive task management board leveraging Angular's new reactive primitive: **Signals**.
*   **Key Highlights**:
    *   `signal<Task[]>`: Reactively stores the tasks database.
    *   `signal.update()`: Modern, immutable state updates instead of direct mutations.
    *   **Native HTML5 Drag & Drop**: Easy card transition across columns.
    *   **SCSS styling**: Styled using custom CSS Grid, SASS variables, and responsive flexboxes.

---

## 🛠️ Tech Stack & Best Practices

*   **Framework**: Angular 19+ (Standalone components, modern APIs)
*   **Styling**: Vanilla SCSS (variables, mixins, nesting, glassmorphism)
*   **State Management**: Signals + Declarative RxJS Observables
*   **Clean Code**:
    *   TypeScript strict mode enabled.
    *   Automatic component unsubscription via `OnDestroy` and `async` pipe.
    *   Responsive layouts (Mobile first).

---

## 💻 Local Setup & Execution

1.  Clone this repository:
    ```bash
    git clone https://github.com/davidzoro9/angular_projets.git
    cd angular_projets
    ```
2.  Install dependencies:
    ```bash
    npm install
    ```
3.  Run the local development server:
    ```bash
    npm run start
    ```
4.  Open your browser and navigate to `http://localhost:4200/`.
