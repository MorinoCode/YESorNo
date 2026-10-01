'use strict';

document.addEventListener('DOMContentLoaded', () => {
  // Tabs
  const tabDirect = document.getElementById('tab-direct');
  const tabQuestion = document.getElementById('tab-question');

  // Panels
  const panelDirect = document.getElementById('panel-direct');
  const panelQuestion = document.getElementById('panel-question');

  // Direct Mode Elements
  const directIdle = document.getElementById('direct-idle');
  const directResult = document.getElementById('direct-result');
  const btnDirectDecide = document.getElementById('btn-direct-decide');
  const btnDirectAgain = document.getElementById('btn-direct-again');
  const btnDirectReset = document.getElementById('btn-direct-reset');
  const directBadge = document.getElementById('direct-badge');
  const directIcon = document.getElementById('direct-icon');
  const directText = document.getElementById('direct-text');

  // Question Mode Elements
  const questionIdle = document.getElementById('question-idle');
  const questionResult = document.getElementById('question-result');
  const questionInput = document.getElementById('question-input');
  const btnQuestionDecide = document.getElementById('btn-question-decide');
  const btnQuestionAgain = document.getElementById('btn-question-again');
  const btnQuestionNew = document.getElementById('btn-question-new');
  const displayQuestion = document.getElementById('display-question');
  const questionBadge = document.getElementById('question-badge');
  const questionIcon = document.getElementById('question-icon');
  const questionText = document.getElementById('question-text');

  // Footer Hint
  const shortcutKey = document.getElementById('shortcut-key');

  // SVG Icons
  const CHECK_ICON = `
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
      <polyline points="20 6 9 17 4 12"></polyline>
    </svg>
  `;

  const CROSS_ICON = `
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
      <line x1="18" y1="6" x2="6" y2="18"></line>
      <line x1="6" y1="6" x2="18" y2="18"></line>
    </svg>
  `;

  // State
  let currentMode = 'direct'; // 'direct' | 'question'
  let lastEnteredQuestion = '';

  /**
   * Generates a cryptographically strong 50/50 decision
   * Returns: 'YES' | 'NO'
   */
  function getRandomDecision() {
    const array = new Uint8Array(1);
    crypto.getRandomValues(array);
    return array[0] % 2 === 0 ? 'YES' : 'NO';
  }

  /**
   * Updates result UI elements instantly (no animation)
   */
  function applyResult(badgeElem, iconElem, textElem, result) {
    if (result === 'YES') {
      badgeElem.className = 'result-badge yes';
      iconElem.innerHTML = CHECK_ICON;
      textElem.textContent = 'YES';
    } else {
      badgeElem.className = 'result-badge no';
      iconElem.innerHTML = CROSS_ICON;
      textElem.textContent = 'NO';
    }
  }

  // --- Direct Mode Handlers ---
  function executeDirectDecide() {
    const decision = getRandomDecision();
    applyResult(directBadge, directIcon, directText, decision);
    directIdle.classList.add('hidden');
    directResult.classList.remove('hidden');
    btnDirectAgain.focus();
  }

  function resetDirect() {
    directResult.classList.add('hidden');
    directIdle.classList.remove('hidden');
    btnDirectDecide.focus();
  }

  // --- Question Mode Handlers ---
  function executeQuestionDecide() {
    const rawVal = questionInput.value.trim();
    lastEnteredQuestion = rawVal || 'Your Question';
    displayQuestion.textContent = lastEnteredQuestion;

    const decision = getRandomDecision();
    applyResult(questionBadge, questionIcon, questionText, decision);

    questionIdle.classList.add('hidden');
    questionResult.classList.remove('hidden');
    btnQuestionAgain.focus();
  }

  function executeQuestionDecideAgain() {
    const decision = getRandomDecision();
    applyResult(questionBadge, questionIcon, questionText, decision);
  }

  function resetQuestion() {
    questionResult.classList.add('hidden');
    questionIdle.classList.remove('hidden');
    questionInput.value = '';
    questionInput.focus();
  }

  // --- Tab Switching ---
  function switchTab(mode) {
    currentMode = mode;
    if (mode === 'direct') {
      tabDirect.classList.add('active');
      tabDirect.setAttribute('aria-selected', 'true');
      tabQuestion.classList.remove('active');
      tabQuestion.setAttribute('aria-selected', 'false');

      panelDirect.classList.remove('hidden');
      panelQuestion.classList.add('hidden');
      shortcutKey.textContent = 'Enter / Space';

      if (directResult.classList.contains('hidden')) {
        btnDirectDecide.focus();
      } else {
        btnDirectAgain.focus();
      }
    } else {
      tabQuestion.classList.add('active');
      tabQuestion.setAttribute('aria-selected', 'true');
      tabDirect.classList.remove('active');
      tabDirect.setAttribute('aria-selected', 'false');

      panelQuestion.classList.remove('hidden');
      panelDirect.classList.add('hidden');
      shortcutKey.textContent = 'Enter';

      if (questionResult.classList.contains('hidden')) {
        questionInput.focus();
      } else {
        btnQuestionAgain.focus();
      }
    }
  }

  // Event Listeners: Tabs
  tabDirect.addEventListener('click', () => switchTab('direct'));
  tabQuestion.addEventListener('click', () => switchTab('question'));

  // Event Listeners: Direct Mode
  btnDirectDecide.addEventListener('click', executeDirectDecide);
  btnDirectAgain.addEventListener('click', executeDirectDecide);
  btnDirectReset.addEventListener('click', resetDirect);

  // Event Listeners: Question Mode
  btnQuestionDecide.addEventListener('click', executeQuestionDecide);
  btnQuestionAgain.addEventListener('click', executeQuestionDecideAgain);
  btnQuestionNew.addEventListener('click', resetQuestion);

  questionInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      executeQuestionDecide();
    }
  });

  // Global Keyboard Navigation
  window.addEventListener('keydown', (e) => {
    // If user is currently typing in an input, let input listener handle Enter
    if (document.activeElement === questionInput) {
      return;
    }

    if (e.key === 'Enter' || (e.key === ' ' && currentMode === 'direct')) {
      e.preventDefault();
      if (currentMode === 'direct') {
        executeDirectDecide();
      } else {
        if (!questionResult.classList.contains('hidden')) {
          executeQuestionDecideAgain();
        } else {
          executeQuestionDecide();
        }
      }
    }
  });

  // Initial focus
  btnDirectDecide.focus();
});
