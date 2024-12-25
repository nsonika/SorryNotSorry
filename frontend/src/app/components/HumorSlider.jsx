"use client";
import React from "react";

const humorLevels = [
    { id: "1", label: "Mild" },
    { id: "2", label: "Witty" },
    { id: "3", label: "Absurd" },
];

export default function HumorSlider({ value, onChange }) {
    return (
        <div className="space-y-4">
            <label className="block text-lg font-medium text-gray-700">Humor Level</label>
            <div className="flex justify-between gap-4">
                {humorLevels.map(({ id, label }) => (
                    <button
                        key={id}
                        onClick={() => onChange(id)}
                        className={`flex-1 py-3 px-4 rounded-lg font-medium transition-all ${value === id
                                ? "bg-indigo-600 text-white scale-105"
                                : "bg-white text-gray-600 hover:bg-gray-50"
                            }`}
                    >
                        {label}
                    </button>
                ))}
            </div>
        </div>
    );
}
