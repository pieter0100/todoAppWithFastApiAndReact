interface TodoCardProps {
    task: string;
    isDone: boolean;
    deleteFunction: () => void;
    toggleDone: () => void;
}

function TodoCard({task, isDone, deleteFunction, toggleDone}: TodoCardProps) {
    return (
        <div className={`todo-card ${isDone ? "done" : ""}`}>
            <span className="todo-card-text">{task}</span>

            <div style={{ display: 'flex', gap: '8px' }}>
                <button onClick={toggleDone}>
                    {isDone ? "Undo" : "Done"}
                </button>
                <button className="delete-btn" onClick={deleteFunction}>
                    Delete
                </button>
            </div>
        </div>
    );
}

export default TodoCard;