"use client";
import React, { useState } from "react";
import { Wand2, Sparkles, Save, RefreshCw, Share2 } from "lucide-react";
import HumorSlider from "./HumorSlider";
import CategorySelector from "./CatergorySelector";
import ContextInput from "./ContextInput";
// import { console } from "inspector";

export default function ExcuseGenerator() {
  const [excuse, setExcuse] = useState("");
  const [humorLevel, setHumorLevel] = useState("1"); // Default to 'Serious'
  const [selectedCategory, setSelectedCategory] = useState("work");
  const [customContext, setCustomContext] = useState("");


  console.log(selectedCategory);
  console.log(humorLevel);
  console.log(customContext);
  

  const generateExcuse = async () => {
    try {
      const response = await fetch(`${process.env.NEXT_PUBLIC_API_BASE_URL}/generate`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          category: selectedCategory,
          humor_level: parseInt(humorLevel, 10),
          custom_context: customContext || undefined,
        }),
      });

      if (!response.ok) {
        throw new Error("Failed to generate excuse");
      }

      const data = await response.json();
      setExcuse(data.excuse);
      console.log(data);
    } catch (error) {
      console.error("Error generating excuse:", error);
      setExcuse("An error occurred while generating the excuse. Please try again.");
    }
  };

  return (
    <div className="max-w-2xl mx-auto p-6 space-y-8">
      <CategorySelector
        selectedCategory={selectedCategory}
        onSelectCategory={setSelectedCategory}
      />

      <HumorSlider value={humorLevel} onChange={setHumorLevel} />

      <ContextInput value={customContext} onChange={setCustomContext} />

      <div className="flex justify-center">
        <button
          onClick={generateExcuse}
          className="flex items-center gap-2 bg-indigo-600 hover:bg-indigo-700 text-white px-6 py-3 rounded-lg font-medium transition-colors"
        >
          <Wand2 className="w-5 h-5" />
          Generate Excuse
        </button>
      </div>

      {excuse && (
        <div className="bg-white p-6 rounded-xl shadow-lg space-y-4">
          <div className="flex items-start gap-3">
            <Sparkles className="w-6 h-6 text-yellow-500 flex-shrink-0 mt-1" />
            <p className="text-xl font-medium text-gray-800">{excuse}</p>
          </div>

          <div className="flex gap-3 justify-end">
            <button
              className="p-2 hover:bg-gray-100 rounded-full transition-colors"
              onClick={generateExcuse} // Refresh to generate a new excuse
            >
              <RefreshCw className="w-5 h-5 text-gray-600" />
            </button>
            <button className="p-2 hover:bg-gray-100 rounded-full transition-colors">
              <Save className="w-5 h-5 text-gray-600" />
            </button>
            <button className="p-2 hover:bg-gray-100 rounded-full transition-colors">
              <Share2 className="w-5 h-5 text-gray-600" />
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
