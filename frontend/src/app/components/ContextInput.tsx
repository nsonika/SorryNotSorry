"use client";
import React from "react";

// Define the type for the props
interface ContextInputProps {
  value: string; // The current value of the input
  onChange: (value: string) => void; // Function to handle changes in the input
}

export default function ContextInput({ value, onChange }: ContextInputProps) {
  return (
    <div className="space-y-3">
      <label className="block text-lg font-medium text-gray-700">
        Custom Context
      </label>
      <textarea
        value={value}
        onChange={(e) => onChange(e.target.value)}
        placeholder="Add specific details for your excuse (e.g., 'meeting with boss', 'friend's birthday party')"
        className="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 min-h-[100px] resize-none"
      />
    </div>
  );
}
