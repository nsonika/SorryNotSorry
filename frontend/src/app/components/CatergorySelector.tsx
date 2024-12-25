"use client";
import React from "react";
import { Briefcase, Users, Heart, Plus } from "lucide-react";

// Define the type for the props
interface CategorySelectorProps {
  selectedCategory: string; // The selected category ID
  onSelectCategory: (id: string) => void; // Function to handle category selection
}

const categories = [
  { id: "work", icon: Briefcase, label: "Work" },
  { id: "social", icon: Users, label: "Social" },
  { id: "relationships", icon: Heart, label: "Relationships" },
  { id: "custom", icon: Plus, label: "Custom" },
];

export default function CategorySelector({
  selectedCategory,
  onSelectCategory,
}: CategorySelectorProps) {
  return (
    <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
      {categories.map(({ id, icon: Icon, label }) => (
        <button
          key={id}
          onClick={() => onSelectCategory(id)}
          className={`flex flex-col items-center p-4 rounded-xl transition-all ${
            selectedCategory === id
              ? "bg-indigo-100 text-indigo-600 scale-105"
              : "bg-white hover:bg-gray-50 text-gray-600"
          }`}
        >
          <Icon className="w-8 h-8 mb-2" />
          <span className="font-medium">{label}</span>
        </button>
      ))}
    </div>
  );
}
